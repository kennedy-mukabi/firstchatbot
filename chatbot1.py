{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi I'm Jessy. Ask me something\n",
      "hello\n",
      "hey you get my snap?\n",
      "happy to hear that\n",
      "its ok\n",
      "bye\n",
      "Bye,Have a nice day!\n"
     ]
    }
   ],
   "source": [
    "from textblob import TextBlob\n",
    "from textblob.classifiers import NaiveBayesClassifier\n",
    "from textblob import Word\n",
    "import random\n",
    "\n",
    "def greetings_check(tb):\n",
    "\tfor word in tb.words:\n",
    "\t\tif word.lower() in GREETING_KEYWORDS:\n",
    "\t\t\treturn random.choice(GREETING_RESPONSES)\n",
    "\n",
    "def reply_engine(sentence,train):\n",
    "    cl = NaiveBayesClassifier(train)\n",
    "    k = str(cl.classify((sentence)))\n",
    "    if k == 'pos':\n",
    "        return random.choice(POSITIVE_RESPONSE)\n",
    "    elif k == 'neg':\n",
    "        return random.choice(NEGATIVE_RESPONSE)\n",
    "\n",
    "\n",
    "train = [\n",
    "     ('I love this sandwich.', 'pos'), ('this is an amazing place!', 'pos'),\n",
    "     ('I feel very good about these beers.', 'pos'),\n",
    "     ('this is my best work.', 'pos'),\n",
    "     (\"what an awesome view\", 'pos'),\n",
    "     ('I do not like this restaurant', 'neg'),\n",
    "     ('I am tired of this stuff.', 'neg'),\n",
    "     (\"I can't deal with this\", 'neg'),\n",
    "     ('he is my sworn enemy!', 'neg'),\n",
    "     ('my boss is horrible.', 'neg'),\n",
    "     (\"i hate you.\",'neg'),\n",
    "     (\"i love mangoes.\",'pos'),\n",
    "     (\"i am sad.\", 'neg')\n",
    "]\n",
    "\n",
    "test = [\n",
    "     ('the beer was good.', 'pos'),\n",
    "     ('I do not enjoy my job', 'neg'),\n",
    "     (\"I ain't feeling dandy today.\", 'neg'),\n",
    "     (\"I feel amazing!\", 'pos'),\n",
    "     ('Gary is a friend of mine.', 'pos'),\n",
    "     (\"I can't believe I'm doing this.\", 'neg')\n",
    "\n",
    "]\n",
    "\n",
    "GREETING_KEYWORDS = (\"hello\",\"hey\", \"hi\", \"greetings\", \"sup\", \"what's up\",\"namaste\")\n",
    "\n",
    "GREETING_RESPONSES = [\"'sup bro\", \"hey\", \"*nods*\", \"hey you get my snap?\"]\n",
    "\n",
    "POSITIVE_RESPONSE = [\"wow thats cool\", \"amazing\", \"you are awesome\", \"happy to hear that\"]\n",
    "NEGATIVE_RESPONSE = [\"thats bad\", \"i am sorry\", \"this is embarassing\", \"its ok\"]\n",
    "\n",
    "\n",
    "\n",
    "print('Hi I\\'m Jessy. Ask me something')\n",
    "sentence = input()\n",
    "\n",
    "while sentence.lower() != 'bye':\n",
    "   tb = TextBlob(sentence)\n",
    "   t = str(greetings_check(tb))\n",
    "   if t == 'None':\n",
    "       t = reply_engine(tb,train)\n",
    "   print(t)\n",
    "   sentence = input()\n",
    "print('Bye,Have a nice day!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
