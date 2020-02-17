import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.(执行API并响应存储请求）
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)


# Store API response in a variable.（以字典的形式打开）
response_dict = r.json()

# Explore information about the repositories.（研究相关仓库信息）
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
   

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],#项目描述
        'xlink': repo_dict['html_url'],#网络链接
        }
    plot_dicts.append(plot_dict)

# Make visualization.(可视化仓库)
my_style = LS('#333366', base_style=LCS)

"""改进pygal图表
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)"""
chart = pygal.Bar( style=my_style)
#chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
