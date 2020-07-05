import re

"""
CleanText class clears all html tags,
special characters,
extra space and change upper letters to lower letters.
For Arabic language
It changes أآإ to ا
and  ة  to  ه
"""


class CleanText:
    def __init__(self, text=""):
        self.text = text

    def clean_text_en(self):
        clean = re.compile('<.*?>')
        self.text = re.sub(clean, '', self.text)
        self.text = re.sub('[^A-Za-z0-9 ]', '', self.text)
        self.text = re.sub(' +', ' ', self.text)
        return self.text.lower()

    def clean_text_ar(self):
        clean = re.compile('<.*?>')
        self.text = re.sub(clean, '', self.text)
        self.text = re.sub('[^\u0621-\u064A0-9 ]', '', self.text)
        self.text = re.sub(' +', ' ', self.text)
        self.text = re.sub('[أآإ]', 'ا', self.text)
        self.text = re.sub('ة', 'ه', self.text)
        return self.text

    def clean_text_ar_en(self):
        clean = re.compile('<.*?>')
        self.text = re.sub(clean, '', self.text)
        self.text = re.sub('[^\u0621-\u064A0-9A-Za-z ]', '', self.text)
        self.text = re.sub(' +', ' ', self.text)
        self.text = re.sub('[أآإ]', 'ا', self.text)
        self.text = re.sub('ة', 'ه', self.text)
        return self.text.lower()


textAr = 'مرحبأ بكم في المدرسة ****        انتم هنا معي >> آنت هنا'
textEn = 'Hello every     one gome//// to my +++    web'
textAR = "مرحبا بكم ---(()))) WELCOME TO my Web Site"
print(CleanText(textAr).clean_text_ar())
print(CleanText(textEn).clean_text_en())
print(CleanText(textAR).clean_text_ar_en())