env:
	export all_proxy="http://127.0.0.1:6152"
tags:
	cd tags && git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git && mv ./a1111-sd-webui-tagcomplete/tags/danbooru.csv ./a1111-sd-webui-tagcomplete/tags/e621.csv ./a1111-sd-webui-tagcomplete/tags/extra-quality-tags.csv . && rm -fr a1111-sd-webui-tagcomplete

