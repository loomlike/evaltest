"""Functional test utilities"""
from typing import Callable, Dict, List

from openai import RateLimitError
import pytest


DEFAULT_REPETITIONS = 3


def assert_score(
    judge_fn: Callable,
    samples: Dict[str, List],
    repetitions: int = DEFAULT_REPETITIONS,
    tolerance: float = 1.0,
):
    """To test the stability of the LLM judge.
    run `repetitions` times and assert the max score differences are <= `tolerance`"""

    num_samples = len(samples["question"])
    scores = [[] for _ in range(num_samples)]
    try:
        for _ in range(repetitions):
            metric_value = judge_fn(data=samples, max_attempts=num_samples)
            for i, score in enumerate(metric_value.scores):
                scores[i].append(score)

        for i, score in enumerate(scores):
            assert (
                max(score) - min(score) <= tolerance
            ), f"Stability test failed for judge {judge_fn.__name__} on sample {i} with scores: {score}"
    except RateLimitError:
        pytest.skip("RateLimitError occurred, skipping test.")
