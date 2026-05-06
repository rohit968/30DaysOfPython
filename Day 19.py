# DAY 19: 30 Days of python programming
import json


# Exercise Level 1

#1
def num_of_lines_and_words(text):
    with open(text) as f:
        lines = f.read()
        num_of_lines = len(lines.split('\n')) # Getting number of lines in text
        num_of_words = len(lines.split()) # Getting number of words in text
        print(num_of_lines, num_of_words)

num_of_lines_and_words('./data/obama_speech.txt')
num_of_lines_and_words('./data/michelle_obama_speech.txt')
num_of_lines_and_words('./data/donald_speech.txt')
num_of_lines_and_words('./data/melina_trump_speech.txt')

#2
def most_spoken_languages(filename, num_of_lang):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
        languages, result = [], []
        for country in countries:
                languages.extend(country['languages'])

        for language in set(languages):
            result.append((languages.count(language), language))
        result.sort(reverse = True)
        print(result[:num_of_lang])

most_spoken_languages('./data/countries_data.json', 10)

#3
def most_populated_countries(filename, num_of_countries):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
        populated_countries = []
        for country in countries:
            populated_countries.append({'country': country['name'], 'population': country['population']})
        sorted_populated_countries = sorted(populated_countries, key = lambda x: x['population'], reverse=True)
        print(sorted_populated_countries[:num_of_countries])

most_populated_countries('./data/countries_data.json', 10)
