from federatedsecure.server.builtins.sync.barrier import Barrier
from federatedsecure.server.builtins.sync.broadcast import Broadcast


def federatedsecure_register(registry):

    registry.register(
        {
            "namespace": "federatedsecure",
            "plugin": "Sync",
            "version": "0.5.3",
            "microservice": "Barrier"
        },
        Barrier()
    )

    registry.register(
        {
            "namespace": "federatedsecure",
            "plugin": "Sync",
            "version": "0.5.3",
            "microservice": "Broadcast"
        },
        Broadcast()
    )
