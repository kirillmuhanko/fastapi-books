from app.controllers_dtos.auth.user_register_request_dto import UserRegisterRequestDto
from app.services_dtos.auth.user_register_service_dto import UserRegisterServiceDto


class ControllerUserMapper:

    @staticmethod
    def to_user_register_service_dto(request_dto: UserRegisterRequestDto) -> UserRegisterServiceDto:
        """
        Maps a UserRegisterRequestDto instance to a UserRegisterServiceDto instance.

        Args:
            request_dto: The UserRegisterRequestDto instance to convert.

        Returns:
            A new UserRegisterServiceDto instance with the mapped data.
        """

        return UserRegisterServiceDto(
            id=0,
            email=request_dto.email,
            username=request_dto.username,
            first_name=request_dto.first_name,
            last_name=request_dto.last_name,
            password=request_dto.password,
            role=request_dto.role
        )
