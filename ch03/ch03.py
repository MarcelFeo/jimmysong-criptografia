{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4f94a28d",
   "metadata": {},
   "outputs": [],
   "source": [
    "class FieldElement:\n",
    "        # retorna se o elemento está no corpo ou não        \n",
    "        def __init__(self, num, prime):\n",
    "            # se o número não existir dentro do corpo ele retorna o erro\n",
    "            if num >= prime or num < 0:\n",
    "               error = 'Num {} not in field range 0 to {}'.format(num, prime-1)\n",
    "               raise ValueError(error)\n",
    "            self.num = num\n",
    "            self.prime = prime\n",
    "            \n",
    "        def __repr__(self):\n",
    "            # retorna o numero presente no corpo e a quantidade de elementos\n",
    "            return 'FieldElement_{}({})'.format(self.prime, self.num)\n",
    "        \n",
    "        def __eq__(self, other):\n",
    "            # compara um numero dentro do corpo com outro numero\n",
    "            if other is None:\n",
    "                return False;\n",
    "            return self.num == other.num and self.prime == other.prime\n",
    "        # Exercício 1\n",
    "        def __ne__(self, other):\n",
    "            raise not (self == other)\n",
    "        # Exercício 2\n",
    "        def __add__(self, other):\n",
    "            if self.prime != other.prime:\n",
    "                raise TypeError('Cannot add two numbers in different Fields')\n",
    "            num = (self.num + other.num) % self.prime\n",
    "            return self.__class__(num, self.prime)\n",
    "        # Exercício 3\\n\",\n",
    "        def __sub__(self, other):\n",
    "            if self.prime != other.prime:\n",
    "                raise TypeError('Cannot sub two numbers in different Fields')\n",
    "            num = (self.num - other.num) % self.prime\n",
    "            return self.__class__(num, self.prime)\n",
    "        # Exercício 4\n",
    "        def __mul__(self, other):\n",
    "            if self.prime != other.prime:\n",
    "                raise TypeError('Cannot mul two numbers in different Fields')            \n",
    "            num = (self.num * other.num) % self.prime\n",
    "            return self.__class__(num, self.prime)\n",
    "        # Exercício 5\n",
    "        def __pow__(self, exponent):           \n",
    "            num = (self.num ** exponent) % self.prime\n",
    "            return self.__class__(num, self.prime)\n",
    "        \n",
    "class Point:\n",
    "    def __init__(self, x, y, a, b):\n",
    "        self.a = a\n",
    "        self.b = b\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        if self.x is None and self.y is None:\n",
    "            return\n",
    "        if self.y**2 != (self.x**3)+(a*x)+b:\n",
    "            error = '({}, {}) is not on the curve'.format(x, y)\n",
    "            raise ValueError(error)\n",
    "\n",
    "class ECCTest:\n",
    "     def test_on_curve(self):\n",
    "         prime = 223\n",
    "         a = FieldElement(0, prime)\n",
    "         b = FieldElement(7, prime)\n",
    "         valid_points = ((192, 105), (17, 56), (1, 193))\n",
    "         invalid_points = ((200, 119), (42, 99))\n",
    "         for x_raw, y_raw in valid_points:\n",
    "             x = FieldElement(x_raw, prime)\n",
    "             y = FieldElement(y_raw, prime)\n",
    "             Point(x, y, a, b)\n",
    "         for x_raw, y_raw in invalid_points:\n",
    "             x = FieldElement(x_raw, prime)\n",
    "             y = FieldElement(y_raw, prime)\n",
    "             with self.assertRaises(ValueError):\n",
    "                 Point(x, y, a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "746d5634",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "exceptions must derive from BaseException",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 5\u001b[0m\n\u001b[0;32m      3\u001b[0m x \u001b[38;5;241m=\u001b[39m FieldElement(num\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m192\u001b[39m, prime\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m223\u001b[39m)\n\u001b[0;32m      4\u001b[0m y \u001b[38;5;241m=\u001b[39m FieldElement(num\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m105\u001b[39m, prime\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m223\u001b[39m)\n\u001b[1;32m----> 5\u001b[0m p1 \u001b[38;5;241m=\u001b[39m \u001b[43mPoint\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43my\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43ma\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28mprint\u001b[39m(p1)\n",
      "Cell \u001b[1;32mIn[17], line 54\u001b[0m, in \u001b[0;36mPoint.__init__\u001b[1;34m(self, x, y, a, b)\u001b[0m\n\u001b[0;32m     52\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mx \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39my \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m     53\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m\n\u001b[1;32m---> 54\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43my\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m!=\u001b[39;49m\u001b[43m \u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m3\u001b[39;49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43ma\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mx\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43mb\u001b[49m:\n\u001b[0;32m     55\u001b[0m     error \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m(\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m, \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m) is not on the curve\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(x, y)\n\u001b[0;32m     56\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(error)\n",
      "Cell \u001b[1;32mIn[17], line 22\u001b[0m, in \u001b[0;36mFieldElement.__ne__\u001b[1;34m(self, other)\u001b[0m\n\u001b[0;32m     21\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__ne__\u001b[39m(\u001b[38;5;28mself\u001b[39m, other):\n\u001b[1;32m---> 22\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m (\u001b[38;5;28mself\u001b[39m \u001b[38;5;241m==\u001b[39m other)\n",
      "\u001b[1;31mTypeError\u001b[0m: exceptions must derive from BaseException"
     ]
    }
   ],
   "source": [
    "a = FieldElement(num=0, prime=223)\n",
    "b = FieldElement(num=7, prime=223)\n",
    "x = FieldElement(num=192, prime=223)\n",
    "y = FieldElement(num=105, prime=223)\n",
    "p1 = Point(x, y, a, b)\n",
    "print(p1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9e97acea",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "exceptions must derive from BaseException",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[14], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m x2 \u001b[38;5;241m=\u001b[39m FieldElement(num\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m17\u001b[39m, prime\u001b[38;5;241m=\u001b[39mprime)\n\u001b[0;32m      7\u001b[0m y2 \u001b[38;5;241m=\u001b[39m FieldElement(num\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m56\u001b[39m, prime\u001b[38;5;241m=\u001b[39mprime)\n\u001b[1;32m----> 8\u001b[0m p1 \u001b[38;5;241m=\u001b[39m \u001b[43mPoint\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx1\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43my1\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43ma\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      9\u001b[0m p2 \u001b[38;5;241m=\u001b[39m Point(x2, y2, a, b)\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28mprint\u001b[39m(p1\u001b[38;5;241m+\u001b[39mp2)\n",
      "Cell \u001b[1;32mIn[13], line 54\u001b[0m, in \u001b[0;36mPoint.__init__\u001b[1;34m(self, x, y, a, b)\u001b[0m\n\u001b[0;32m     52\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mx \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39my \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m     53\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m\n\u001b[1;32m---> 54\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43my\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m!=\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m3\u001b[39;49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[43ma\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mx\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m:\n\u001b[0;32m     55\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m(\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m, \u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m) is not on the curve\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(x, y))\n",
      "Cell \u001b[1;32mIn[13], line 22\u001b[0m, in \u001b[0;36mFieldElement.__ne__\u001b[1;34m(self, other)\u001b[0m\n\u001b[0;32m     21\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__ne__\u001b[39m(\u001b[38;5;28mself\u001b[39m, other):\n\u001b[1;32m---> 22\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m (\u001b[38;5;28mself\u001b[39m \u001b[38;5;241m==\u001b[39m other)\n",
      "\u001b[1;31mTypeError\u001b[0m: exceptions must derive from BaseException"
     ]
    }
   ],
   "source": [
    "prime = 223\n",
    "a = FieldElement(num=0, prime=prime)\n",
    "b = FieldElement(num=7, prime=prime)\n",
    "x1 = FieldElement(num=192, prime=prime)\n",
    "y1 = FieldElement(num=105, prime=prime)\n",
    "x2 = FieldElement(num=17, prime=prime)\n",
    "y2 = FieldElement(num=56, prime=prime)\n",
    "p1 = Point(x1, y1, a, b)\n",
    "p2 = Point(x2, y2, a, b)\n",
    "print(p1+p2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f45c4747",
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
