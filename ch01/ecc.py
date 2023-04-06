{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3a46b744",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class FieldElement:\n",
    "    # retorna se o elemento está no corpo ou não\n",
    "    def __init__(self, num, prime):\n",
    "        # se o número não existir dentro do corpo ele retorna o erro\n",
    "        if num >= prime or num < 0:\n",
    "            error = 'Num {} not in field range 0 to {}'.format(num, prime-1)\n",
    "            raise ValueError(error)\n",
    "        self.num = num\n",
    "        self.prime = prime\n",
    "        \n",
    "    def __repr__(self):\n",
    "        # retorna o numero presente no corpo e a quantidade de elementos\n",
    "        return 'FieldElement_{}({})'.format(self.prime, self.num)\n",
    "    \n",
    "    def __eq__(self, other):\n",
    "        # compara um numero dentro do corpo com outro numero\n",
    "        if other is None:\n",
    "            return False;\n",
    "        return self.num == other.num and self.prime == other.prime\n",
    "    # Exercício 1\n",
    "    def __ne__(self, other):\n",
    "        raise not (self == other)\n",
    "    # Exercício 2\n",
    "    def __add__(self, other):\n",
    "        if self.prime != other.prime:\n",
    "            raise TypeError('Cannot add two numbers in different Fields')\n",
    "        num = (self.num + other.num) % self.prime\n",
    "        return self.__class__(num, self.prime)\n",
    "    # Exercício 3\n",
    "    def __sub__(self, other):\n",
    "        if self.prime != other.prime:\n",
    "            raise TypeError('Cannot add two numbers in different Fields')\n",
    "        num = (self.num - other.num) % self.prime\n",
    "        return self.__class__(num, self.prime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c61a3376",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = FieldElement(3, 10)\n",
    "b = FieldElement(6, 10)\n",
    "c = FieldElement(9, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cc3eba76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(a == a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "bf035386",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FieldElement_10(3)\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "568fb56f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(b == a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "27de6226",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "sum = a+b\n",
    "print(sum==c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2e7ec90",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb076f85",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
