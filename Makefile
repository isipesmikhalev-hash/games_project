install:
	uv sync

VD-games:
	 vd-main

build:
	uv build

package-install:
	uv tool install dist/*.whl
