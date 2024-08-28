# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from llama_toolchain.distribution.datatypes import RemoteProviderConfig


async def get_adapter_impl(config: RemoteProviderConfig, _deps):
    from .ollama import OllamaInferenceAdapter

    impl = OllamaInferenceAdapter(config.url)
    await impl.initialize()
    return impl
