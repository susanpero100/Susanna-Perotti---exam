def click_through_rate(clicks: int, impressions: int) -> float:
    if clicks < 0:
        raise ValueError("clicks must not be negative")
    if impressions <= 0:
        raise ValueError("impressions must be greater than zero")
    return (clicks / impressions) * 100


def count_campaign_tags(tags: list[str]) -> int:
    return len(tags)


def normalize_campaign_name(campaign_name: str | None) -> str:
    if campaign_name is None:
        return ""
    return campaign_name.strip()
