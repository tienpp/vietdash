# -*- encoding: utf-8 -*-
#TODO: gạch chân tên riêng
word_dict = open('vv30K.index', 'r').readlines()

def dash(source_text):
	for line in word_dict:
		word = line.split('\t')[0]
		if ' ' in word:
			#Các dấu kết thúc câu
			#regex replace welcome!!!
			tmp_word = [' ' + word + ' ']
			tmp_word += [' ' + word + '.']
			tmp_word += [' ' + word + ',']
			tmp_word += [' ' + word + '!']
			tmp_word += [' ' + word + ';']
			tmp_word += [' ' + word + '?']
			tmp_word += [' ' + word + ')']
			tmp_word += ['(' + word + ' ']
			#Phần dưới tạo ra list các từ, để phòng trường hợp các từ ghép ngắn hơn được gạch ngang trước
			#ví dụ A Di -> A Di thì sau đó A Di Đà không replace được nữa
			for i in range(word.count(' ')):
				tmp_word += [' ' + word.replace(' ', '-', i+1) + ' ']
				tmp_word += [' ' + word.replace(' ', '-', i+1) + '.']
				tmp_word += [' ' + word.replace(' ', '-', i+1) + ',']
				tmp_word += [' ' + word.replace(' ', '-', i+1) + '!']
				tmp_word += [' ' + word.replace(' ', '-', i+1) + ';']
				tmp_word += [' ' + word.replace(' ', '-', i+1) + '?']
				tmp_word += [' ' + word.replace(' ', '-', i+1) + ')']
				tmp_word += ['(' + word.replace(' ', '-', i+1) + ' ']
			for gen_word in tmp_word:
				#đầu câu thì viết hoa
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				word_start = [gen_word[1:].replace(gen_word[1:][0], gen_word[1:][0].upper(), 1)]
				if gen_word in source_text:
					sdf = ' ' + gen_word[1:-1].replace(' ', '-') + gen_word[-1]
					source_text = source_text.replace(gen_word, sdf)
				else:
					for word in word_start:
						if word in source_text:
							if word[-1] == ' ':
								sdf = word[:-1].replace(' ', '-') + ' '
							else:
								sdf = word[:-1].replace(' ', '-') + word[-1]
							source_text = source_text.replace(word, sdf)

	return source_text

if __name__ == '__main__':
	source_text = open('ex', 'r').read()
	out_text = dash(source_text)
	f = open('gachout', 'wb')
	f.write(out_text)
	f.close()