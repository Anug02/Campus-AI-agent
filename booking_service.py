{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d38efbf3-ef0a-44c7-b532-7fb656351d87",
   "metadata": {},
   "outputs": [],
   "source": [
    "from data_sources import BOOKINGS_DB\n",
    "\n",
    "def create_booking(user, resource_id, date, time):\n",
    "    booking = {\n",
    "        \"user\": user,\n",
    "        \"resource_id\": resource_id,\n",
    "        \"date\": date,\n",
    "        \"time\": time\n",
    "    }\n",
    "    BOOKINGS_DB.append(booking)\n",
    "    return booking\n"
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
