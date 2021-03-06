from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar, Union

from django.http import HttpResponse
from typing_extensions import TypedDict

ViewFuncT = TypeVar('ViewFuncT', bound=Callable[..., HttpResponse])

# See zerver/lib/validator.py for more details of Validators,
# including many examples
Validator = Callable[[str, object], Optional[str]]
ExtendedValidator = Callable[[str, str, object], Optional[str]]
RealmUserValidator = Callable[[int, List[int], bool], Optional[str]]

class ProfileDataElementBase(TypedDict):
    id: int
    name: str
    type: int
    hint: Optional[str]
    field_data: Optional[str]
    order: int

class ProfileDataElement(ProfileDataElementBase):
    value: str
    rendered_value: Optional[str]

ProfileData = List[ProfileDataElement]

FieldElement = Tuple[int, str, Validator, Callable[[Any], Any], str]
ExtendedFieldElement = Tuple[int, str, ExtendedValidator, Callable[[Any], Any], str]
UserFieldElement = Tuple[int, str, RealmUserValidator, Callable[[Any], Any], str]

ProfileFieldData = Dict[str, Union[Dict[str, str], str]]

class UserDisplayRecipient(TypedDict):
    email: str
    full_name: str
    short_name: str
    id: int
    is_mirror_dummy: bool
DisplayRecipientT = Union[str, List[UserDisplayRecipient]]
