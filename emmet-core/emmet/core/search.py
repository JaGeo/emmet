from typing import Dict, List, Optional, TypeVar, Union

from pydantic import BaseModel, Field
from pymatgen.analysis.magnetism.analyzer import Ordering
from pymatgen.core.periodic_table import Element
from pymatgen.core.structure import Structure

from emmet.core.electronic_structure import BandstructureData, DosData
from emmet.core.material_property import PropertyDoc
from emmet.core.mpid import MPID
from emmet.core.thermo import DecompositionProduct
from emmet.core.xas import Edge, Type

T = TypeVar("T", bound="SearchDoc")


class SearchSummary(BaseModel):
    """
    Statistics about a specified SearchDoc field.
    """

    field: str = Field(
        None,
        title="Field",
        description="Field name corresponding to a field in SearchDoc",
    )
    num_samples: Optional[int] = Field(
        None,
        title="Sample",
        description="The number of documents sampled to generate statistics. "
        "If unspecified, statistics will be from entire database.",
    )
    min: float = Field(
        None,
        title="Minimum",
        description="The minimum value "
        "of the specified field used to "
        "generate statistics.",
    )
    max: float = Field(
        None,
        title="Maximum",
        description="The maximum value "
        "of the specified field used to "
        "generate statistics.",
    )
    median: float = Field(
        None, title="Median", description="The median of the field values."
    )
    mean: float = Field(None, title="Mean", description="The mean of the field values.")
    distribution: List[float] = Field(
        None,
        title="Distribution",
        description="List of floats specifying a kernel density "
        "estimator of the distribution, equally spaced "
        "between specified minimum and maximum values.",
    )


class XASSearchData(BaseModel):
    """
    Fields in XAS sub docs in search
    """

    edge: Edge = Field(
        None, title="Absorption Edge", description="The interaction edge for XAS"
    )
    absorbing_element: Element = Field(None, title="Absorbing Element")

    spectrum_type: Type = Field(None, title="Type of XAS Spectrum")


class GBSearchData(BaseModel):
    """
    Fields in grain boundary sub docs in search
    """

    sigma: int = Field(None, description="Sigma value of the boundary")

    type: str = Field(None, description="Grain boundary type")

    gb_energy: float = Field(None, description="Grain boundary energy in J/m^2")

    rotation_angle: float = Field(None, description="Rotation angle in degrees")


class SearchDoc(PropertyDoc):
    """
    Summary information about materials and their properties, useful for materials
    screening studies and searching.
    """

    # Materials

    deprecated: bool = Field(
        ..., description="Whether the material is tagged as deprecated"
    )
    structure: Structure = Field(
        ..., description="The lowest energy structure for this material"
    )

    # Thermo

    uncorrected_energy_per_atom: float = Field(
        None, description="The total DFT energy of this material per atom in eV/atom"
    )

    energy_per_atom: float = Field(
        None,
        description="The total corrected DFT energy of this material per atom in eV/atom",
    )

    formation_energy_per_atom: float = Field(
        None, description="The formation energy per atom in eV/atom"
    )

    energy_above_hull: float = Field(
        None, description="The energy above the hull in eV/Atom"
    )

    is_stable: bool = Field(
        False,
        description="Flag for whether this material is on the hull and therefore stable",
    )

    equillibrium_reaction_energy_per_atom: float = Field(
        None,
        description="The reaction energy of a stable entry from the neighboring equilibrium stable materials in eV."
        " Also known as the inverse distance to hull.",
    )

    decomposes_to: List[DecompositionProduct] = Field(
        None,
        description="List of decomposition data for this material. Only valid for metastable or unstable material.",
    )

    # XAS

    xas: List[XASSearchData] = Field(None, description="List of xas documents.")

    # GB

    grain_boundaries: List[GBSearchData] = Field(
        None, description="List of grain boundary documents."
    )

    # Electronic Structure

    band_gap: float = Field(None, description="Band gap energy in eV.")

    cbm: Union[float, Dict] = Field(None, description="Conduction band minimum data.")

    vbm: Union[float, Dict] = Field(None, description="Valence band maximum data.")

    efermi: float = Field(None, description="Fermi energy eV.")

    is_gap_direct: bool = Field(None, description="Whether the band gap is direct.")

    is_metal: bool = Field(None, description="Whether the material is a metal.")

    magnetic_ordering: Union[str, Ordering] = Field(
        None, description="Magnetic ordering of the calculation."
    )

    es_source_calc_id: Union[MPID, int] = Field(
        None, description="The source calculation ID for the electronic structure data."
    )

    bandstructure: BandstructureData = Field(
        None, description="Band structure data for the material."
    )

    dos: DosData = Field(None, description="Density of states data for the material.")

    # DOS

    dos_energy_up: float = Field(None, description="Spin-up DOS band gap.")

    dos_energy_down: float = Field(None, description="Spin-down DOS band gap.")

    # Magnetism

    ordering: str = Field(None, description="Type of magnetic ordering.")

    total_magnetization: float = Field(None, description="Total magnetization in μB.")

    total_magnetization_normalized_vol: float = Field(
        None, description="Total magnetization normalized by volume in μB/Å³."
    )

    total_magnetization_normalized_formula_units: float = Field(
        None, description="Total magnetization normalized by formula unit in μB/f.u. ."
    )

    # Elasticity

    k_voigt: float = Field(None, description="Voigt average of the bulk modulus.")

    k_reuss: float = Field(
        None, description="Reuss average of the bulk modulus in GPa."
    )

    k_vrh: float = Field(
        None, description="Voigt-Reuss-Hill average of the bulk modulus in GPa."
    )

    g_voigt: float = Field(
        None, description="Voigt average of the shear modulus in GPa."
    )

    g_reuss: float = Field(
        None, description="Reuss average of the shear modulus in GPa."
    )

    g_vrh: float = Field(
        None, description="Voigt-Reuss-Hill average of the shear modulus in GPa."
    )

    universal_anisotropy: float = Field(None, description="Elastic anisotropy.")

    homogeneous_poisson: float = Field(None, description="Poisson's ratio.")

    # Dielectric and Piezo

    e_total: float = Field(None, description="Total dielectric constant")

    e_ionic: float = Field(None, description="Ionic contributio to dielectric constant")

    e_static: float = Field(
        None, description="Electronic contribution to dielectric constant"
    )

    n: float = Field(None, description="Refractive index")

    e_ij_max: float = Field(None, description="Piezoelectric modulus")

    # Surface Properties

    weighted_surface_energy_EV_PER_ANG2: float = Field(
        None, description="Weighted surface energy in eV/Å²"
    )

    weighted_surface_energy: float = Field(
        None, description="Weighted surface energy in J/m²"
    )

    weighted_work_function: float = Field(
        None, description="Weighted work function in eV."
    )

    surface_anisotropy: float = Field(None, description="Surface energy anisotropy.")

    shape_factor: float = Field(None, description="Shape factor.")

    # Has Props

    has_props: List[str] = Field(
        None, description="List of properties that are available for a given material."
    )

    # Theoretical

    theoretical: bool = Field(True, description="Whether the material is theoretical.")

    @classmethod
    def from_docs(cls, material_id: MPID, **docs: Dict[str, Dict]):
        """Converts a bunch of search docs into a SearchDoc"""
        doc = _copy_from_doc(docs)

        # Reshape document for various sub-sections
        # Electronic Structure + Bandstructure + DOS
        doc["electronic_structure"] = {
            k: v for sub_doc in doc["electronic_structure"] for k, v in sub_doc.items()
        }
        if "bandstructure" in doc:
            doc["has_props"].append("bandstructure")
        if "dos" in doc:
            doc["has_props"].append("dos")
        if "calc_id" in doc:
            doc["es_source_calc_id"] = doc["calc_id"]
            del doc["calc_id"]

        # Magnetism
        doc["spin_polarized"] = "magnetism" in doc

        doc["has_props"] = list(set(doc["has_props"]))

        return SearchDoc(material_id=material_id, **doc)


# Key mapping
search_fields: Dict[str, list] = {
    "materials": [
        "nsites",
        "elements",
        "nelements",
        "composition",
        "composition_reduced",
        "formula_pretty",
        "formula_anonymous",
        "chemsys",
        "volume",
        "density",
        "density_atomic",
        "symmetry",
        "structure",
        "deprecated",
    ],
    "thermo": [
        "uncorrected_energy_per_atom",
        "energy_per_atom",
        "formation_energy_per_atom",
        "energy_above_hull",
        "is_stable",
        "equillibrium_reaction_energy_per_atom",
        "decomposes_to",
    ],
    "xas": ["absorbing_element", "edge", "spectrum_type", "xas_id"],
    "grain_boundaries": [
        "gb_energy",
        "sigma",
        "type",
        "rotation_angle",
        "w_sep",
    ],
    "electronic_structure": [
        "band_gap",
        "efermi",
        "cbm",
        "vbm",
        "is_gap_direct",
        "is_metal",
        "bandstructure",
        "dos",
        "calc_id",
        "bandstructure",
        "dos",
    ],
    "magnetism": [
        "ordering",
        "total_magnetization",
        "total_magnetization_normalized_vol",
        "total_magnetization_normalized_formula_units",
    ],
    "elasticity": [
        "k_voigt",
        "k_reuss",
        "k_vrh",
        "g_voigt",
        "g_reuss",
        "g_vrh",
        "universal_anisotropy",
        "homogeneous_poisson",
    ],
    "dielectric": ["e_total", "e_ionic", "e_static", "n"],
    "piezoelectric": ["e_ij_max"],
    "surface_properties": [
        "weighted_surface_energy",
        "weighted_surface_energy_EV_PER_ANG2",
        "shape_factor",
        "surface_anisotropy",
    ],
    "eos": [],
    "phonon": [],
    "insertion_electrodes": [],
    "substrates": [],
}


def _copy_from_doc(doc):
    """Helper functin to copy the list of keys over from amalgamated document"""
    d = {"has_props": []}
    # Complex function to grab the keys and put them in the root doc
    # if the item is a list, it makes one doc per item with those corresponding keys
    for sub_doc in search_fields:
        if sub_doc in doc:
            d["has_props"].append(sub_doc)
            if isinstance(search_fields[sub_doc], list):
                d[sub_doc] = []
                for sub_item in search_fields[sub_doc]:
                    temp_doc = {
                        copy_key: sub_item[copy_key]
                        for copy_key in search_fields[sub_doc]
                        if copy_key in sub_item
                    }
                    d[sub_doc].append(temp_doc)
            else:
                d.update(
                    {
                        copy_key: d[sub_doc][copy_key]
                        for copy_key in search_fields[sub_doc]
                        if copy_key in d[sub_doc]
                    }
                )
    return d
