from datetime import timedelta

def format_duration(seconds):
    """
    Convierte segundos a formato minutos:segundos (MM:SS)
    """
    if seconds is None:
        return "00:00"
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def parse_duration(duration_str):
    """
    Convierte formato MM:SS a segundos
    """
    try:
        minutes, seconds = map(int, duration_str.split(':'))
        return minutes * 60 + seconds
    except:
        return 0

def format_file_size(size_in_bytes):
    """
    Formatea el tamaño de archivo en bytes a una representación legible
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} TB"

def get_pagination_params(request, default_per_page=10):
    """
    Obtiene parámetros de paginación de la solicitud
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default_per_page, type=int)
    return page, per_page