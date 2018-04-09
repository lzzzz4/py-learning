import jieba
from matplotlib.image import imread
from wordcloud import WordCloud, ImageColorGenerator
# 必须手动导入
import matplotlib.pyplot as plt

# 添加过滤词 之后会改至txt中
my_filter = ['那么', '便是', '忽然', '有些', '不过', '却是', '知道', '这是', '略微', '如果', '而且', '有着',
             '这种', '虽然', '然后', '一些', '什么', '不是']
# 读小说,读背景图片
novel_path = "H:/斗破苍穹.txt"
img_path = "H:/atom.jpg"
# 添加新词
jieba.add_word("萧炎哥哥")


def filter_stop_word(mywords):
    result = ""
    for word in mywords:
        if word not in my_filter:
            result += word
            result += " "
    return result


novel_text = open(novel_path, "r").read()
words = jieba.cut(novel_text)
# 得到wordline 即一行要生成词云的字符串
# 不过滤词语
# word_line = " ".join(word)
# 过滤词语得到字符串
word_line = filter_stop_word(words)
# 读背景图片
bg_pic = imread(img_path)

# 生成词云
wordcloud = WordCloud(font_path='msyh.ttc', mask=bg_pic, background_color='white', scale=1.5,
                      max_font_size=100).generate(word_line)
image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
# 保存图片
wordcloud.to_file('H:/test.jpg')
