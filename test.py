# install flair
# pip3 install flair

import flair
sentiment_model = flair.models.TextClassifier.load('en-sentiment')
sentence = flair.data.Sentence('you suck')
sentiment_model.predict(sentence)
print(sentence)

sentence = flair.data.Sentence('Tesla delivered 201,250 vehicles in the second quarter, up from the prior record of 184,800 in the first quarter. Deliveries soared 120% from the year-ago period')
sentiment_model.predict(sentence)
print(sentence)


sentence = flair.data.Sentence('Tesla stock dipped 3% despite the earnings announcement on July 2 but it has since regained that ground.')
sentiment_model.predict(sentence)
print(sentence)


