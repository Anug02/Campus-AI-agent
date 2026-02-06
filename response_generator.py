{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "599f2abf-ab8a-48b4-b1c8-4edc3bb2954b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_response(intent, data=None):\n",
    "    if intent == \"events\":\n",
    "        return {\"events\": data}\n",
    "    elif intent == \"facilities\":\n",
    "        return {\"facilities\": data}\n",
    "    elif intent == \"booking\":\n",
    "        return {\"message\": \"Booking confirmed\", \"details\": data}\n",
    "    else:\n",
    "        return {\"message\": \"Sorry, I couldn't understand your request.\"}\n"
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
