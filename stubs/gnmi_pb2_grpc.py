# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gnmi_pb2 as gnmi__pb2

GRPC_GENERATED_VERSION = '1.73.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gnmi_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class gNMIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Capabilities = channel.unary_unary(
                '/gnmi.gNMI/Capabilities',
                request_serializer=gnmi__pb2.CapabilityRequest.SerializeToString,
                response_deserializer=gnmi__pb2.CapabilityResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/gnmi.gNMI/Get',
                request_serializer=gnmi__pb2.GetRequest.SerializeToString,
                response_deserializer=gnmi__pb2.GetResponse.FromString,
                _registered_method=True)
        self.Set = channel.unary_unary(
                '/gnmi.gNMI/Set',
                request_serializer=gnmi__pb2.SetRequest.SerializeToString,
                response_deserializer=gnmi__pb2.SetResponse.FromString,
                _registered_method=True)
        self.Subscribe = channel.stream_stream(
                '/gnmi.gNMI/Subscribe',
                request_serializer=gnmi__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=gnmi__pb2.SubscribeResponse.FromString,
                _registered_method=True)


class gNMIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Capabilities(self, request, context):
        """Capabilities allows the client to retrieve the set of capabilities that
        is supported by the target. This allows the target to validate the
        service version that is implemented and retrieve the set of models that
        the target supports. The models can then be specified in subsequent RPCs
        to restrict the set of data that is utilized.
        Reference: gNMI Specification Section 3.2
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Retrieve a snapshot of data from the target. A Get RPC requests that the
        target snapshots a subset of the data tree as specified by the paths
        included in the message and serializes this to be returned to the
        client using the specified encoding.
        Reference: gNMI Specification Section 3.3
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Set allows the client to modify the state of data on the target. The
        paths to modified along with the new values that the client wishes
        to set the value to.
        Reference: gNMI Specification Section 3.4
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request_iterator, context):
        """Subscribe allows a client to request the target to send it values
        of particular paths within the data tree. These values may be streamed
        at a particular cadence (STREAM), sent one off on a long-lived channel
        (POLL), or sent as a one-off retrieval (ONCE).
        Reference: gNMI Specification Section 3.5
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_gNMIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Capabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.Capabilities,
                    request_deserializer=gnmi__pb2.CapabilityRequest.FromString,
                    response_serializer=gnmi__pb2.CapabilityResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=gnmi__pb2.GetRequest.FromString,
                    response_serializer=gnmi__pb2.GetResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=gnmi__pb2.SetRequest.FromString,
                    response_serializer=gnmi__pb2.SetResponse.SerializeToString,
            ),
            'Subscribe': grpc.stream_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=gnmi__pb2.SubscribeRequest.FromString,
                    response_serializer=gnmi__pb2.SubscribeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gnmi.gNMI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gnmi.gNMI', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class gNMI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Capabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gnmi.gNMI/Capabilities',
            gnmi__pb2.CapabilityRequest.SerializeToString,
            gnmi__pb2.CapabilityResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gnmi.gNMI/Get',
            gnmi__pb2.GetRequest.SerializeToString,
            gnmi__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gnmi.gNMI/Set',
            gnmi__pb2.SetRequest.SerializeToString,
            gnmi__pb2.SetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Subscribe(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/gnmi.gNMI/Subscribe',
            gnmi__pb2.SubscribeRequest.SerializeToString,
            gnmi__pb2.SubscribeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
