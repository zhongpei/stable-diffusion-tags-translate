tags:
	cd tags && git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git && mv ./a1111-sd-webui-tagcomplete/tags/danbooru.csv ./a1111-sd-webui-tagcomplete/tags/e621.csv ./a1111-sd-webui-tagcomplete/tags/extra-quality-tags.csv . && rm -fr a1111-sd-webui-tagcomplete

env:
	python -m "venv" && source venv/bin/activate && pip install -r requirements.txt

gen:
	python better_prompt_translate.py
	python booru_translate.py

gen-no-google:
	export USE_GOOGLE_TRANSLATE=false && python better_prompt_translate.py && python booru_translate.py

gpt:
	TRANSLATE_CACHE_DIR=./cache.gpt4 USE_REDIS_CACHE=true all_proxy="http://127.0.0.1:6152" python gpt4_data_translate.py
