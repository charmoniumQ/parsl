from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from parsl.executors.workqueue.executor import WorkQueueExecutor
    from parsl.executors.high_throughput.executor import HighThroughputExecutor
    from parsl.executors.threads import ThreadPoolExecutor
    from parsl.executors.extreme_scale.executor import ExtremeScaleExecutor

lazys = {
    'ThreadPoolExecutor': 'parsl.executors.threads',
    'WorkQueueExecutor': 'parsl.executors.workqueue.executor',
    'HighThroughputExecutor': 'parsl.executors.high_throughput.executor',
    'ExtremeScaleExecutor': 'parsl.executors.extreme_scale.executor',
    'LowLatencyExecutor': 'parsl.executors.low_latency.executor',
    'FluxExecutor': 'parsl.executors.flux.executor',
}

import parsl.executors as px


def lazy_loader(name):
    if name in lazys:
        import importlib
        m = lazys[name]
        print(f"lazy load {name} from module {m}")
        v = importlib.import_module(m)
        print(f"imported module: {v}")
        a = v.__getattribute__(name)
        px.__setattr__(name, a)
        return a
    raise AttributeError(f"No (lazy loadable) attribute in {__name__} for {name}")


px.__getattr__ = lazy_loader

__all__ = ['ThreadPoolExecutor',
           'HighThroughputExecutor',
           'ExtremeScaleExecutor',
           'LowLatencyExecutor',
           'WorkQueueExecutor',
           'FluxExecutor']
