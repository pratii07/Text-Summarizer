import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation 
from heapq import nlargest
from string import punctuation
print(punctuation)

text = """Marvel's The Avengers[5] (titled Marvel Avengers Assemble in the United Kingdom and Ireland[1][6] and 
            commonly referred to as simply The Avengers) is a 2012 American superhero film based on the Marvel Comics 
            superhero team of the same name. Produced by Marvel Studios and distributed by Walt Disney Studios Motion
            Pictures,[a] it is the sixth film in the Marvel Cinematic Universe (MCU). Written and directed by Joss Whedon, 
            the film features an ensemble cast including Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett 
            Johansson, and Jeremy Renner as the Avengers, alongside Tom Hiddleston, Stellan Skarsgård, and Samuel L. Jackson. 
            In the film, Nick Fury and the spy agency S.H.I.E.L.D. recruit Tony Stark, Steve Rogers, Bruce Banner, Thor, Natasha
            Romanoff, and Clint Barton to form a team capable of stopping Thor's brother Loki from subjugating Earth.
            The Avengers premiered at the El Capitan Theatre in Los Angeles on April 11, 2012, and was released in the United States 
            on May 4, as the final film in Phase One of the MCU. The film received praise for Whedon's direction and screenplay, visual effects,
            action sequences, acting, and musical score. It grossed over $1.5 billion worldwide, setting numerous box office 
            records and becoming."""

def summarizer(text):
    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    # print(doc)
    tokens = [token.text for token in doc]
    # print(tokens) 
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text] += 1
    # print(word_freq)
    max_frequency = max(word_freq.values())
    # print(max_frequency)
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_frequency
    # print(word_freq)
    sentence_list = [sentence for sentence in doc.sents]
    # print(sentence_list)  
    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_freq[word.text]
                else:
                    sentence_scores[sent] += word_freq[word.text]           
    # print(sentence_scores)
    select_length = int(len(sentence_list)*0.3)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print("Summary :")
    # print(summary)
    # print("Length of original text : ", len(text))
    # print("Length of summary : ", len(summary))
    # print("Compression ratio : ", len(summary)/len(text))
    # print("Percentage of compression : ", (len(text) - len(summary))/len(text)*100)
    return summary , doc , len(text.split(' ')), len(summary.split(' ')) 
