"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List

# Example schemas (you can keep or remove these if not needed)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# --------------------------------------------------
# Pictiv.Studio Schemas
# --------------------------------------------------

class Service(BaseModel):
    """Services offered by the studio
    Collection: "service"
    """
    name: str
    category: str = Field(..., description="wedding | pre-wedding | maternity | portrait | event | custom")
    description: str
    deliverables: List[str] = []
    duration_minutes: Optional[int] = Field(None, ge=15, description="Expected duration in minutes")
    price: Optional[float] = Field(None, ge=0, description="Base price if applicable")
    addons: List[str] = []
    is_active: bool = True

class Booking(BaseModel):
    """Client booking requests
    Collection: "booking"
    """
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    service_name: Optional[str] = Field(None, description="Selected service name")
    preferred_date: str = Field(..., description="YYYY-MM-DD")
    preferred_time: Optional[str] = Field(None, description="HH:MM")
    location: Optional[str] = None
    notes: Optional[str] = None
    status: str = Field("pending", description="pending | confirmed | cancelled")

class GalleryItem(BaseModel):
    url: str
    title: Optional[str] = None
    watermark: bool = True

class Gallery(BaseModel):
    """Private client galleries
    Collection: "gallery"
    """
    code: str = Field(..., description="Shareable access code")
    client_name: str
    package: Optional[str] = None
    allow_download: bool = False
    items: List[GalleryItem] = []

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
