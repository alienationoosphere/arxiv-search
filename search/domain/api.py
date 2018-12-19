"""API-specific domain classes."""

from .base import DateRange, Query, ClassificationList, List
from .advanced import FieldedSearchList, FieldedSearchTerm

from dataclasses import dataclass, field
from typing import NamedTuple, Optional


def get_default_extra_fields() -> List[str]:
    """These are the default extra fields."""
    return ['title']


def get_required_fields() -> List[str]:
    """These fields should always be included."""
    return ['paper_id', 'paper_id_v', 'version', 'href', 'canonical']


@dataclass
class APIQuery(Query):
    """
    Represents an API query.

    Similar to an advanced query.
    """

    date_range: Optional[DateRange] = None
    classification: ClassificationList = field(
        default_factory=ClassificationList
    )
    include_cross_list: bool = field(default=True)
    terms: FieldedSearchList = field(default_factory=FieldedSearchList)
    include_fields: List[str] = field(default_factory=get_default_extra_fields)

    def __post_init__(self) -> None:
        """Be sure that the required fields are prepended to include_fields."""
        self.include_fields = list(
            set(get_required_fields() + self.include_fields)
        )
