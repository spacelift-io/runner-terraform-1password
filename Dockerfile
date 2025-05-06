FROM public.ecr.aws/spacelift/runner-terraform:latest

ARG TARGETARCH
ARG OP_VERSION=2.30.3

USER root

RUN wget "https://cache.agilebits.com/dist/1P/op2/pkg/v${OP_VERSION}/op_linux_${TARGETARCH}_v${OP_VERSION}.zip" -O op.zip && \
    unzip -d op op.zip && \
    mv op/op /usr/local/bin/ && \
    rm -r op.zip op && \
    chmod g+s /usr/local/bin/op && \
    op --version

USER spacelift
