FROM buildpack-deps:18.04 AS base
# Note: using isolinux instead of syslinux
RUN apt update && apt install -y mkisofs isolinux
# Get iPXE source and Enable extra supports
WORKDIR /workspace
# Use a stable version
ARG GIT_TAG="-b v1.20.1"
RUN git clone -q $GIT_TAG --single-branch --depth=1 http://git.ipxe.org/ipxe.git \
    && perl -pe -i 's@//(?=#define (?:NSLOOKUP_CMD|PING_CMD))@@' ipxe/src/config/general.h


FROM base AS build
WORKDIR /workspace
ARG ENDPOINT
ARG CHANNEL
# Note: Put embedded script into ipxe/src
RUN echo "#!ipxe\ndhcp\nchain http://$ENDPOINT/$CHANNEL/boot.ipxe" > ipxe/src/chain.ipxe
RUN cd ipxe/src && make -j6 bin/ipxe.iso EMBED=chain.ipxe


FROM base AS iso
WORKDIR /iso
VOlUME /iso
# Note: put artifact to volume dir using CMD
# rather than COPY or RUN that only executes command in the intermediate layer
COPY --from=build /workspace/ipxe/src/bin/ipxe.iso /tmp
CMD [ "cp", "/tmp/ipxe.iso", "/iso/" ]
