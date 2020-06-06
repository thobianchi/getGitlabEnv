NAME    := gitlabctl
PACKAGE := github.com/thobianchi/$(NAME)
GIT     := $(shell git rev-parse --short HEAD)
DATE    := $(shell date -u +%FT%T%Z)
VERSION  ?= $(shell git describe --tags)
IMG_NAME := thobianchi/gitlabctl
IMAGE    := ${IMG_NAME}:${VERSION}

default: help

test:   ## Run all tests
	@go clean --testcache && go test -race ./...

cover:  ## Run test coverage suite
	@go test ./... -race --coverprofile=cov.out
	@go tool cover --html=cov.out

build:  ## Builds the CLI
	@go build \
	-ldflags "-w -s -X ${PACKAGE}/cmd.version=${VERSION} -X ${PACKAGE}/cmd.commit=${GIT} -X ${PACKAGE}/cmd.date=${DATE}" \
	-a -tags netgo -o bin/${NAME} main.go

img:    ## Build Docker Image
	@docker build --rm -t ${IMAGE} .

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":[^:]*?## "}; {printf "\033[38;5;69m%-30s\033[38;5;38m %s\033[0m\n", $$1, $$2}'
