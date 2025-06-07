from .controller_hotel import HotelViewSet
from .controller_personal import PersonalViewSet
from .controller_habitacion import HabitacionViewSet
from .controller_reserva import ReservaViewSet
from .controller_huesped import HuespedViewSet
from .controller_pago import PagoViewSet

__all__ = [
    'HotelViewSet',
    'PersonalViewSet',
    'HabitacionViewSet',
    'ReservaViewSet',
    'HuespedViewSet',
    'PagoViewSet',
]