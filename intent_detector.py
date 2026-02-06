{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e26d0cd-506d-45e6-a18b-dd92f88f5dea",
   "metadata": {},
   "outputs": [],
   "source": [
    "import spacy\n",
    "\n",
    "nlp = spacy.load(\"en_core_web_sm\")\n",
    "\n",
    "INTENT_KEYWORDS = {\n",
    "    \"events\": [\"event\", \"seminar\", \"workshop\", \"conference\"],\n",
    "    \"facilities\": [\"lab\", \"room\", \"facility\", \"library\"],\n",
    "    \"booking\": [\"book\", \"reserve\", \"register\"]\n",
    "}\n",
    "\n",
    "def detect_intent(text: str):\n",
    "    text_lower = text.lower()\n",
    "    for intent, keywords in INTENT_KEYWORDS.items():\n",
    "        if any(word in text_lower for word in keywords):\n",
    "            return intent\n",
    "    return \"unknown\"\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
