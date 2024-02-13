"""
HPO toolkit is a library for working with Human Phenotype Ontology and the HPO annotation data.
"""

__version__ = "0.4.4dev0"

from . import algorithm
from . import annotations
from . import constants
from . import graph
from . import model
from . import ontology
from . import util
from . import validate

from .graph import OntologyGraph, GraphAware
from .model import TermId, Term, MinimalTerm, Synonym, SynonymType, SynonymCategory
from .ontology import Ontology, MinimalOntology

from .ontology.load.obographs import load_minimal_ontology, load_ontology
