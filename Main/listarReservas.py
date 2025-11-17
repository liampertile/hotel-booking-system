from shared.mysql_connection import select

def listarReservas():
    reservas = select(
            "SELECT * FROM reserva WHERE estado = 'confirmada'   AND CURDATE() >= DATE(fecha_check_in)   AND CURDATE() <  DATE(fecha_check_out);")
    print("Reservas actuales:\n")
    for reserva in reservas:
        print(f"• Reserva: {reserva[0]}, Habitación: {reserva[1]}, ID Cliente: {reserva[2]}, Duración [{reserva[6]}, {reserva[7]}], Estado: {reserva[4]}\n")