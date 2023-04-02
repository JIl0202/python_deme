# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function is called.")
#         result = func(*args, **kwargs)
#         print("After the function is called.")
#         return result
#
#     return wrapper
#
# @my_decorator
# def my_function(a,b,c):
#     print("Hello world!")
#
#
# my_function()

#
# from operator import itemgetter
#
# my_list = [{'name': 'Alice', 'age': 25, 'gender': 'female'},
#            {'name': 'Bob', 'age': 30, 'gender': 'male'},
#            {'name': 'Charlie', 'age': 20, 'gender': 'male'},
#            {'name': 'David', 'age': 35, 'gender': 'male'},
#            {'name': 'Eva', 'age': 27, 'gender': 'female'}]
#
# sorted_list = sorted(my_list, key=itemgetter('gender','age'))
# print(sorted_list)

import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.example.com')
        print(html)

if __name__ == '__main__':
    asyncio.run(main())
