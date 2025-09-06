from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import sys
import os


spark = SparkSession.builder.appName("ProductsAndCategories").getOrCreate()

products_data = [(1, "Ноутбук"), (2, "Мышь"), (3, "Клавиатура"),
                     (4, "Наушники"), (5, "Флешка"), (6, "Книга"),(7,'Ручка')]
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])

categories_data = [(1, "Электроника"), (2, "Компьютерная техника"),
                       (3, "Периферия"), (4, "Аксессуары"),(5,'Недвижимость')]

categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])

relations_data = [(1, 1), (1, 2), (2, 3), (2, 4),
                    (3, 3), (4, 1), (4, 4), (5, 4)]

relations_df = spark.createDataFrame(relations_data, ["product_id", "category_id"])

def get_products_and_categories(products_df,categories_df,relations_df):
    product_and_categories = (relations_df.join(products_df,'product_id','full').join(categories_df,'category_id','left').select('product_name','category_name'))
    return product_and_categories


result_df = get_products_and_categories(products_df,categories_df,relations_df)
print("Продукты:")
products_df.show()

print("\nКатегории:")
categories_df.show()

print("\nСвязи:")
relations_df.show()

print("\nРезультат:")
result_df.show()

spark.stop()
