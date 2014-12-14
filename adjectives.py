import nltk
import nltk.classify
import sys
import operator

def write_adjectives(reviews):
    f1 = open('POS/adj_list1.txt', 'w')
    f2 = open('POS/adj_list2.txt', 'w')
    f3 = open('POS/adj_list3.txt', 'w')
    f4 = open('POS/adj_list4.txt', 'w')
    f5 = open('POS/adj_list5.txt', 'w')

    for review in reviews[1]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='JJ':
                f1.write(assignment[0] + ' ')

    for review in reviews[2]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='JJ':
                f2.write(assignment[0] + ' ')

    for review in reviews[3]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='JJ':
                f3.write(assignment[0] + ' ')

    for review in reviews[4]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='JJ':
                f4.write(assignment[0] + ' ')

    for review in reviews[5]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='JJ':
                f5.write(assignment[0] + ' ')
       
