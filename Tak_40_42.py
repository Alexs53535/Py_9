# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "# Задача 40\n",
        "\n",
        "Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)"
      ],
      "metadata": {
        "id": "kji9T2Gd_lPc"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "rx9sXMg3_Kn6"
      },
      "outputs": [],
      "source": [
        "import pandas as pd"
      ]
    },
      {
      "cell_type": "code",
      "source": [
        "file_path = '/content/sample_data/california_housing_train.csv'\n",
        "df = pd.read_csv(file_path, sep=',')"
      ],
      "metadata": {
        "id": "dsgqqhLQ_wyK"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['population'].min()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "flLWsYG8BH2e",
        "outputId": "2680d833-98c2-4328-f489-f5bd29812fdf"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.0"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[df['population'] < 500].median_house_value.mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P0ra4xwR_6OP",
        "outputId": "3f1743a2-d07e-4997-c3fb-4ff2a2aa5175"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "206683.83635227982"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Задача 42\n",
        "Узнать какая максимальная households в зоне минимального значения population"
      ],
      "metadata": {
        "id": "Uf8jpTET_gAX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df[df['population'] == df['population'].min()].households.max()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wHFsj-NZB1pn",
        "outputId": "a917770e-977f-4e55-e221-2c75019023ac"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.0"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    }
  ]
}