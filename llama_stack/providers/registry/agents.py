# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import List

from llama_stack.distribution.datatypes import Api, InlineProviderSpec, ProviderSpec
from llama_stack.providers.utils.kvstore import kvstore_dependencies


def available_providers() -> List[ProviderSpec]:
    return [
        InlineProviderSpec(
            api=Api.agents,
            provider_id="meta-reference",
            pip_packages=[
                "matplotlib",
                "pillow",
                "pandas",
                "scikit-learn",
            ]
            + kvstore_dependencies(),
            module="llama_stack.providers.impls.meta_reference.agents",
            config_class="llama_stack.providers.impls.meta_reference.agents.MetaReferenceAgentsImplConfig",
            api_dependencies=[
                Api.inference,
                Api.safety,
                Api.memory,
            ],
        ),
    ]
