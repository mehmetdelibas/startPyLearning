# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('_mpl-gallery')

# # Make data for a double helix
# n = 50
# theta = np.linspace(0, 2*np.pi, n)
# x1 = np.cos(theta)
# y1 = np.sin(theta)
# z1 = np.linspace(0, 1, n)
# x2 = np.cos(theta + np.pi)
# y2 = np.sin(theta + np.pi)
# z2 = z1

# # Plot
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.fill_between(x1, y1, z1, x2, y2, z2, alpha=0.5)
# ax.plot(x1, y1, z1, linewidth=2, color='C0')
# ax.plot(x2, y2, z2, linewidth=2, color='C0')

# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])

# plt.show()

# print(__name__)

# import requests
# try :
#     myUrl = 'https://www.w3schools.com/python/demopage.htm'
#     result = requests.get(myUrl)
#     result.raise_for_status()
# except requests.exceptions.HTTPError as e:
#     print("Http Hatasi : ",e)
# except Exception as err:
#     print("Başka bir hata oluştu ",err)
# else:
#     print("İstek başarılı")

# print(result.status_code)
# print(result.apparent_encoding)
# print(result.encoding)
# print(result.cookies)
# print(result.elapsed)
# print(result.headers)
# print(result.is_permanent_redirect)
# print(result.is_redirect)
# print(result.status_code)

# for item in result.iter_lines():
#     print(item)

# print(result.json())

# print(result.reason)
# print(result.url)

# result.close()

