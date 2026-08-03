from fastapi import APIRouter

from backend.services.lip_sync_service import LipSyncService

router = APIRouter(
    prefix="/lipsync",
    tags=["Lip Sync Detection"]
)

service = LipSyncService()


@router.get("/health")
def health():

    return {
        "status": "Lip Sync Service Running"
    }


@router.get("/demo")
def demo():

    return service.analyze("sample.mp4")