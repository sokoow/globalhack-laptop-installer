.PHONY: help
.DEFAULT_GOAL := all

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
        match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
        if match:
                target, help = match.groups()
                print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

BUILD_ARGS :=
DOCKER_BUILD = DOCKER_BUILDKIT=1 docker build $(BUILD_ARGS) -t $@ --target iso $(<D)
include configs/current_release

# Need to assign HTTP SERVER IP
all: private BUILD_ARGS := --build-arg ENDPOINT=$(ENDPOINT) --build-arg CHANNEL=$(CHANNEL)
all: configs ## build release of artifacts
	@echo "Ensure http://${ENDPOINT:? please run make with 'ENDPOINT=<ip>'}/${CHANNEL:? please run make with 'CHANNEL=<channel_name>'}.ipxe is available before installing $(CHANNEL).iso"
	@python3 scripts/gen_embedded_script.py configs/$(CHANNEL)/gen_embedded.json dist/$(CHANNEL)/
	$(DOCKER_BUILD)
	@docker run --rm -v $(CURDIR)/dist/$(CHANNEL):/iso iso
	@isohybrid $(CURDIR)/dist/$(CHANNEL)/ipxe.iso
	@zip $(CURDIR)/dist/$(CHANNEL)/$(CHANNEL).zip dist/$(CHANNEL)/ipxe.iso -j
