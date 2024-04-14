import openai
from .models import GrammarRule,WordG

def generate_kazakh_grammar_and_words(self):
    grammar_response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Explain a grammar rule in Kazakh concerning nouns.",
        temperature=0.5,
        max_tokens=100
    )
    grammar_rule_text = grammar_response.choices[0].text.strip()
    grammar_rule = GrammarRule.objects.create(rule_text=grammar_rule_text)

    words_response = openai.Completion.create(
        model="text-davinci-003",
        prompt="List five nouns in Kazakh with their English translations.",
        temperature=0.5,
        max_tokens=100
    )
    words_list = words_response.choices[0].text.strip().split('\n')
    words_objects = [WordG(kazakh_word=kazakh, english_translation=english)
                     for kazakh, english in (word.split(' - ') for word in words_list)]

    WordG.objects.bulk_create(words_objects)

    return grammar_rule, words_objects