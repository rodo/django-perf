WITH rowa AS (
        SELECT h.id, hc.name color, hs.name skin
        from hotel_hotel h
        inner join hotel_hotelcolor hc on hc. id = h.color_id
        inner join hotel_hotelskin hs on hs.id = h.skin_id
        where hc.id=13
        ORDER BY h.id LIMIT 25 OFFSET 20
    )
    select array_to_json(rowa.*) from rowa
