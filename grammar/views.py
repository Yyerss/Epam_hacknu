import requests
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GrammarRule, WordG
from datetime import datetime
from .serializer import WordSerializer, GrammarRuleSerializer
from django.conf import settings


class DailyGrammarAndWords(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.today().date()
        words = WordG.objects.filter(date_added=today)

        if not words.exists():
            grammar_rule, words = self.generate_kazakh_grammar_and_words()

        try:
            grammar_rule = GrammarRule.objects.latest('id')
        except ObjectDoesNotExist:
            grammar_rule = None

        words = WordG.objects.filter(date_added=today)

        words_serializer = WordSerializer(words, many=True)
        grammar_serializer = None if grammar_rule is None else GrammarRuleSerializer(grammar_rule)

        return Response({
            'grammar': grammar_serializer.data if grammar_serializer else None,
            'words': words_serializer.data
        })

    def generate_kazakh_grammar_and_words(self):
        api_key = settings.OPENAI_API_KEY

        url = "https://api.openai.com/v1/engines/text-davinci-002/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        grammar_payload = {
            "prompt": "Explain a grammar rule in Kazakh concerning nouns.",
            "temperature": 0.5,
            "max_tokens": 100,
            "top_p": 1.0,
            "n": 1,
            "stop": ["\n"]
        }

        grammar_response = requests.post(url, json=grammar_payload, headers=headers)

        words_payload = {
            "prompt": "List five nouns in Kazakh with their English translations.",
            "temperature": 0.5,
            "max_tokens": 100,
            "top_p": 1.0,
            "n": 1,
            "stop": ["\n"]
        }

        words_response = requests.post(url, json=words_payload, headers=headers)

        if grammar_response.status_code == 200 and words_response.status_code == 200:
            grammar_rule_text = grammar_response.json()["choices"][0]["text"].strip()
            grammar_rule = GrammarRule.objects.create(rule_text=grammar_rule_text)

            words_list = words_response.json()["choices"][0]["text"].strip().split('\n')
            words_objects = [WordG(kazakh_word=kazakh, english_translation=english)
                             for kazakh, english in (word.split(' - ') for word in words_list)]

            WordG.objects.bulk_create(words_objects)

            return grammar_rule, words_objects
        else:
            if grammar_response.status_code != 200:
                print("Grammar Error:", grammar_response.text)
            if words_response.status_code != 200:
                print("Words Error:", words_response.text)

            return None, None