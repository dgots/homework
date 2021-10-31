import  jieba

txt='''
    真是闲处光阴易过，倏忽又是元宵佳节。士隐令家人霍启抱了英莲，去看社火花灯。半夜中霍启因要小解，
便将英莲放在一家门槛上坐着。待他小解完了来抱时，那有英莲的踪影？急的霍启直寻了半夜。至天明不见，
那霍启也不敢回来见主人，便逃往他乡去了。那士隐夫妇见女儿一夜不归，便知有些不好；再使几人去找寻，
回来皆云影响全无。夫妻二人半世只生此女，一旦失去，何等烦恼，因此昼夜啼哭，几乎不顾性命。
'''
words = jieba.lcut(txt)     
counts = {}     
for word in words:
    if  len(word) == 1:    
        continue
    else:
        counts[word] = counts.get(word, 0) +1
        
items = list(counts.items())
print(items)