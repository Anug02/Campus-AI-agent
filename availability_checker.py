{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28fa68cc-624e-49bb-8c3e-e074e963cff1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_availability(resource_id, date, time, bookings):\n",
    "    for booking in bookings:\n",
    "        if (\n",
    "            booking[\"resource_id\"] == resource_id\n",
    "            and booking[\"date\"] == date\n",
    "            and booking[\"time\"] == time\n",
    "        ):\n",
    "            return False\n",
    "    return True\n"
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
