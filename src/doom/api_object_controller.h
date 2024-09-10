#include "api.h"

api_response_t API_PostObject(cJSON *req);
api_response_t API_GetObjects(int max_distance);
api_response_t API_PatchObject(int id, cJSON *req);
api_response_t API_DeleteObject(int id);
api_response_t API_GetObject(int id);
api_response_t API_GetLineOfSightToObject(int id, int id2);
api_response_t API_GetCheckTraverse(int id, float x, float y);