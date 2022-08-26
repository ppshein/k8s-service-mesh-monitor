# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha1StorageVersionStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'common_encoding_version': 'str',
        'conditions': 'list[V1alpha1StorageVersionCondition]',
        'storage_versions': 'list[V1alpha1ServerStorageVersion]'
    }

    attribute_map = {
        'common_encoding_version': 'commonEncodingVersion',
        'conditions': 'conditions',
        'storage_versions': 'storageVersions'
    }

    def __init__(self, common_encoding_version=None, conditions=None, storage_versions=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1StorageVersionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._common_encoding_version = None
        self._conditions = None
        self._storage_versions = None
        self.discriminator = None

        if common_encoding_version is not None:
            self.common_encoding_version = common_encoding_version
        if conditions is not None:
            self.conditions = conditions
        if storage_versions is not None:
            self.storage_versions = storage_versions

    @property
    def common_encoding_version(self):
        """Gets the common_encoding_version of this V1alpha1StorageVersionStatus.  # noqa: E501

        If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality.  # noqa: E501

        :return: The common_encoding_version of this V1alpha1StorageVersionStatus.  # noqa: E501
        :rtype: str
        """
        return self._common_encoding_version

    @common_encoding_version.setter
    def common_encoding_version(self, common_encoding_version):
        """Sets the common_encoding_version of this V1alpha1StorageVersionStatus.

        If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality.  # noqa: E501

        :param common_encoding_version: The common_encoding_version of this V1alpha1StorageVersionStatus.  # noqa: E501
        :type: str
        """

        self._common_encoding_version = common_encoding_version

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1StorageVersionStatus.  # noqa: E501

        The latest available observations of the storageVersion's state.  # noqa: E501

        :return: The conditions of this V1alpha1StorageVersionStatus.  # noqa: E501
        :rtype: list[V1alpha1StorageVersionCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1StorageVersionStatus.

        The latest available observations of the storageVersion's state.  # noqa: E501

        :param conditions: The conditions of this V1alpha1StorageVersionStatus.  # noqa: E501
        :type: list[V1alpha1StorageVersionCondition]
        """

        self._conditions = conditions

    @property
    def storage_versions(self):
        """Gets the storage_versions of this V1alpha1StorageVersionStatus.  # noqa: E501

        The reported versions per API server instance.  # noqa: E501

        :return: The storage_versions of this V1alpha1StorageVersionStatus.  # noqa: E501
        :rtype: list[V1alpha1ServerStorageVersion]
        """
        return self._storage_versions

    @storage_versions.setter
    def storage_versions(self, storage_versions):
        """Sets the storage_versions of this V1alpha1StorageVersionStatus.

        The reported versions per API server instance.  # noqa: E501

        :param storage_versions: The storage_versions of this V1alpha1StorageVersionStatus.  # noqa: E501
        :type: list[V1alpha1ServerStorageVersion]
        """

        self._storage_versions = storage_versions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1StorageVersionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1StorageVersionStatus):
            return True

        return self.to_dict() != other.to_dict()
