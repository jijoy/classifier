__author__ = 'jlchandr'
from textblob.classifiers import NaiveBayesClassifier


def read_train_data(file):
    train = []
    try:
        lines = open(file,"r", encoding='utf-8').readlines()
    except UnicodeDecodeError:
        lines = open(file,"r", encoding='latin-1').readlines()
    for line in lines[1:]:
        content = line.split(';')[0]
        classifier_class = line.split(';')[1].lower()
        train.append((content,classifier_class))
    cl = NaiveBayesClassifier(train)
    return cl

def classify_data(file,classifier):
    fear_count = 0
    no_fear_count = 0
    try:
        lines = open(file,"r", encoding='utf-8').readlines()
    except UnicodeDecodeError:
        lines = open(file,"r", encoding='latin-1').readlines()
    for line in lines[1:]:
        content = line.split(';')[0]
        print(line)
        result = classifier.classify(content)
        print(result)
        # print(result.strip()=="fear")

        if result.strip()=="fear":
            fear_count += 1
        else:
            no_fear_count += 1

    print('--------Summary--------------------')
    print('Tweets classified under fear = %s'%fear_count)
    print('Tweets classified under no fear  = %s'%no_fear_count)
    print('------------------------------------')

if __name__ == '__main__':
    classifier = read_train_data('ebola_content and classification.csv')
    classify_data('testing_data_set_content_only_limited.csv',classifier)