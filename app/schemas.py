from pydantic import BaseModel, Field

class ProjectItem(BaseModel):
    id: str = Field(..., description="Unique project ID")
    type_projet: str = Field(..., description="Type of project (Renovation, Neuf, etc.)")
    surface_m2: float = Field(..., description="Surface in square meters")
    cout_total: float = Field(..., description="Total cost for the project")
