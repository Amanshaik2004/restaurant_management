from fastapi import FastAPI

from database import Base
from database import engine

import models

from routers.auth_router import router as auth_router
from routers.role_router import router as role_router
from routers.restaurant_router import router as restaurant_router
from routers.restaurant_table_router import router as restaurant_table_router
from routers.category_router import router as category_router
from routers.menu_item_router import router as menu_item_router
from routers.order_router import router as order_router
from routers.bill_router import router as bill_router
from routers.inventory_router import router as inventory_router
from routers.report_router import router as report_router
from routers.notification_router import router as notification_router
from routers.audit_log_router import router as audit_log_router



app = FastAPI(
    title="Restaurant Management System"
)

app.include_router(auth_router)
app.include_router(role_router)
app.include_router(restaurant_router)
app.include_router(restaurant_table_router)
app.include_router(category_router)
app.include_router(menu_item_router)
app.include_router(order_router)
app.include_router(bill_router)
app.include_router(inventory_router)
app.include_router(report_router)
app.include_router(notification_router)
app.include_router(audit_log_router)

Base.metadata.create_all(bind=engine)