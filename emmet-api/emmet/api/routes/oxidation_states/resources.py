from maggma.api.resource import ReadOnlyResource
from emmet.core.oxidation_states import OxidationStateDoc

from maggma.api.query_operator import (
    PaginationQuery,
    SortQuery,
    SparseFieldsQuery,
)

from emmet.api.routes.materials.query_operators import FormulaQuery, ChemsysQuery, MultiMaterialIDQuery
from emmet.api.routes.oxidation_states.query_operators import PossibleOxiStateQuery
from emmet.api.core.global_header import GlobalHeaderProcessor
from emmet.api.core.settings import MAPISettings


def oxi_states_resource(oxi_states_store):
    resource = ReadOnlyResource(
        oxi_states_store,
        OxidationStateDoc,
        query_operators=[
            MultiMaterialIDQuery(),
            FormulaQuery(),
            ChemsysQuery(),
            PossibleOxiStateQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(OxidationStateDoc, default_fields=["material_id", "last_updated"]),
        ],
        header_processor=GlobalHeaderProcessor(),
        tags=["Oxidation States"],
        disable_validation=True,
        timeout=MAPISettings().TIMEOUT,
    )

    return resource
