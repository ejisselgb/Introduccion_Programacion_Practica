{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNztpbR5qnebHiEPtPSTLoE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ejisselgb/Introduccion_Programacion_Practica/blob/main/ClasePython.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PpqDjG-kIHWV",
        "outputId": "6f51317d-ad16-4463-9dc6-0054d5556c60"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingresa un numero: 3000\n",
            "El resultado del producto uno es:  570.0\n",
            "Ingresa un numero: 3000\n",
            "El resultado del producto es:  570.0\n",
            "Ingresa un numero: 3000\n",
            "El resultado del producto es:  570.0\n",
            "El valor total de iva a pagar es:  1710.0\n",
            "El valor total a pagar es:  10710.0\n"
          ]
        }
      ],
      "source": [
        "numero1= float(input(\"Ingresa un numero: \"))\n",
        "producto1= numero1*0.19\n",
        "print(\"El resultado del producto uno es: \", producto1)\n",
        "\n",
        "numero2= float(input(\"Ingresa un numero: \"))\n",
        "producto2= numero2*0.19\n",
        "print(\"El resultado del producto es: \", producto2)\n",
        "\n",
        "numero3= float(input(\"Ingresa un numero: \"))\n",
        "producto3= numero3*0.19\n",
        "print(\"El resultado del producto es: \", producto3)\n",
        "\n",
        "sumasproductos= numero1+numero2+numero3\n",
        "sumaivas= producto1+producto2+producto3\n",
        "\n",
        "print(\"El valor total de iva a pagar es: \", sumaivas)\n",
        "print(\"El valor total a pagar es: \", sumasproductos+sumaivas)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numero1= int(input(\"Ingresa un numero: \"))\n",
        "numero2= int(input(\"Ingresa un numero: \"))\n",
        "\n",
        "suma= numero1+numero2\n",
        "\n",
        "print(\"El resultado de la suma es: \", suma)\n",
        "\n",
        "numero1= int(input(\"Ingresa un numero: \"))\n",
        "numero2= int(input(\"Ingresa un numero: \"))\n",
        "\n",
        "resta= numero1-numero2\n",
        "print(\"El resultado de la resta es: \", resta)\n",
        "\n",
        "division= suma/resta\n",
        "print(\"El resultado de la division es: \", division)\n",
        "multiplicacion= suma*resta\n",
        "print(\"El resultado de la multiplicacion es: \", multiplicacion)\n"
      ],
      "metadata": {
        "id": "d69ZW9b0RVh4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numero1= float(input(\"Ingresa un numero: \"))\n",
        "numero2= float(input(\"Ingresa un numero: \"))\n",
        "numero3= float(input(\"Ingresa un numero: \"))\n",
        "\n",
        "corte1= ((numero1+numero2+numero3)/3)*(0.2)\n",
        "print(\"El resultado del corte uno es: \", corte1)\n",
        "\n",
        "numero1= float(input(\"Ingresa un numero: \"))\n",
        "numero2= float(input(\"Ingresa un numero: \"))\n",
        "numero3= float(input(\"Ingresa un numero: \"))\n",
        "\n",
        "corte2= ((numero1+numero2+numero3)/3)*(0.2)\n",
        "print(\"El resultado del corte dos es: \", corte2)\n",
        "\n",
        "numero1= float(input(\"Ingresa un numero: \"))\n",
        "numero2= float(input(\"Ingresa un numero: \"))\n",
        "numero3= float(input(\"Ingresa un numero: \"))\n",
        "\n",
        "corte3= ((numero1+numero2+numero3)/3)*(0.6)\n",
        "print(\"El resultado del corte tres es: \", corte3)\n",
        "\n",
        "suma= corte1+corte2+corte3\n",
        "print(\"El resultado de total es: \", suma)\n"
      ],
      "metadata": {
        "id": "WV23dveFRVv2"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}